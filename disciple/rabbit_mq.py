import sys
import logging
import pika
import config

logging.basicConfig(level=logging.DEBUG)
channel = None

def on_connected(connection):
    logging.debug('Connected to RabbitMQ')
    connection.channel(on_channel_open)

def on_channel_open(new_channel):
    logging.debug('Channel Opened')
    global channel
    channel = new_channel
    channel.exchange_declare(exchange=config.RABBITMQ_EXCHANGE, exchange_type='fanout', durable=True, callback=on_exchange_declared)

def on_exchange_declared(frame):
    logging.debug('Exchange declared')
    channel.queue_declare(queue=config.RABBITMQ_QUEUE, durable=True, exclusive=False, auto_delete=False, callback=on_queue_declared)

def on_queue_declared(frame):
    logging.debug('Queue declared')
    channel.queue_bind(exchange=config.RABBITMQ_EXCHANGE, queue=config.RABBITMQ_QUEUE, callback=on_queue_bind)

def on_queue_bind(frame):
    logging.debug('Queue bound')
    channel.basic_consume(handle_delivery, queue=config.RABBITMQ_QUEUE)

def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    logging.debug('Message received {}: {}'.format(method.routing_key, body))

    if method.routing_key in routing_key_function_dict:
        routing_key_function_dict[method.routing_key](channel, method, header, body)
    else:
        logging.debug('no message handler found for routing key {}'.format(method.routing_key))


def on_disciple_connected(channel, method, header, body):
    logging.debug('on_disciple_connected')
    echo_message(channel, method.routing_key, body)

def on_disciple_verified(channel, method, header, body):
    logging.debug('on_disciple_verified')
    echo_message(channel, method.routing_key, body)

def on_disciple_processed(channel, method, header, body):
    logging.debug('on_disciple_processed')
    echo_message(channel, method.routing_key, body)

def on_disciple_trained(channel, method, header, body):
    logging.debug('on_disciple_trained')
    echo_message(channel, method.routing_key, body)

def on_disciple_predicted(channel, method, header, body):
    logging.debug('on_disciple_predicted')
    echo_message(channel, method.routing_key, body)

def echo_message(channel, routing_key, body):
    channel.basic_publish(config.RABBITMQ_EXCHANGE,
                          routing_key + '_response',
                          body,
                          pika.BasicProperties(content_type='text/plain',
                                                 delivery_mode=1))

def start():
    parameters = pika.URLParameters(config.RABBITMQ_URL)
    connection = pika.SelectConnection(parameters, on_connected)

    global routing_key_function_dict

    routing_key_function_dict = {
        'disciple.connected': on_disciple_connected,
        'disciple.verified': on_disciple_verified,
        'disciple.processed': on_disciple_processed,
        'disciple.trained': on_disciple_trained,
        'disciple.predicted': on_disciple_predicted
    }

    try:
        connection.ioloop.start()
    except KeyboardInterrupt:
        connection.close()
        connection.ioloop.start()
