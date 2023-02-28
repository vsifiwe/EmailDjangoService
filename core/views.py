from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
import environ


@api_view(["POST"])
def sendEmail(request):
    try:
        email = request.data["email"]
        total = request.data["total"]
        start_month = request.data["start"]
        end_month = request.data["end"]

        message = Mail(
            from_email="emanzi@andrew.cmu.edu",
            to_emails=email,
            subject="Thank you - Student Fund",
            html_content=f"""
            <html>
                <body>
                    <h1
                        style="height: 100px; color: white; background-color: #be112e; padding: 25px;"
                        >
                        Thank you for your contribution to the student fund
                    </h1>
                    <div>
                        <img style="height: 300px;" src="http://cdn.mcauto-images-production.sendgrid.net/5627e370e2222be0/b386a169-0fe4-41ae-8a88-fa3e43f4867f/800x615.png" alt="alternatetext">
                        <h2>Your contribution of the amount of {total} RWF</h2>
                        <h2>for the month of {start_month} to {end_month} has been received</h2>
                    </div>
                </body>
            </html>
            """,
        )
        env = environ.Env()
        api_key = env("SENDGRID_API_KEY")

        sg = SendGridAPIClient(api_key)
        print(api_key)
        response = sg.send(message)
        print(response.body)

    except KeyError:
        return Response({"message": "send all data"})
    except Exception as e:
        return Response({"message": f"error ocurred: {e}"})

    response = {"message": "Success"}

    return Response(response)
