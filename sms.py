from typing import ClassVar, List
import boto3
import sys
import csv

def send(filepath):
    try:
        sns_client = boto3.client("sns")
        with open(filepath[1], mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(sns_client.set_sms_attributes(
                    attributes={
                        'DefaultSMSType': 'Promotional'
                    }
                ))
                print(sns_client.publish(
                    PhoneNumber=row["phone"],
                    Message="Kestrl 2.0 is here! Please delete your current version of Kestrl and re-install it from the AppStore bit.ly/ktrl-ios & GooglePlay bit.ly/kstrl-andr",
                ))

    except IndexError as e:
        print("Please specify a csv file")

if __name__ == '__main__':
    send(sys.argv)