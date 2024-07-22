def lambda_handler(event, context):
    print("Hello. How are you?")

    return {
        "statusCode": 200,
        "body": "Fine, thanks."
    }


if __name__ == "__main__":
    result = lambda_handler(None, None)
    print(result["body"])
