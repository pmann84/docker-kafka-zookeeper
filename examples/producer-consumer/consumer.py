from kafka import KafkaConsumer
from json import loads

def main():
	consumer = KafkaConsumer(
        'number_topic',
         bootstrap_servers=['localhost:9092'],
         auto_offset_reset='earliest',
         enable_auto_commit=True,
         group_id='my-group',
         value_deserializer=lambda x: loads(x.decode('utf-8')))
    
	for message in consumer:
		print(f"Recieved message {message.value}")
        
        
if __name__ == "__main__":
    main()