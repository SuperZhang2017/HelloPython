import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')
print("waiting  for message")

def callback(ch,method,properties,body):
    print("Received",body)

channel.basic_consume(callback,queue='hello',no_ack=True)

channel.start_consuming()
