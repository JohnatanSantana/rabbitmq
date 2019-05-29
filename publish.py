#!pip install pika

import pika

#credenciais
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)      

#conexão com o server
channel = connection.channel()

#declarando queue
#channel.queue_declare(queue='brokersql')

#gerando uma lista para publicar varias mensagens
rang = list(range(0,6000))

for i in rang:
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello JJohn!{}'.format(i))
