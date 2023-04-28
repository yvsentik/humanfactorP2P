# на хуй не надо дискорд убрали
from dhooks import Webhook, Embed

def send_message(description):

    webhook=Webhook('https://discord.com/api/webhooks/1027652261121380382/aILHJqL8JY9W7LKCX5eo3MgFNrUxEGtUKP_Q8TOe4mTz6ZBfowG8AupwKF8x-MRTaWWp')
    embed = Embed(
        title = 'Binance' ,
        description = description,
        color = 0x5CDBF0
    )

    webhook.send(embed=embed)