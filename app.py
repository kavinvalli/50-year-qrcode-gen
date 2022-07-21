from PIL import Image, ImageFont, ImageDraw
import qrcode
import json
import os

from twilio.rest import Client

title_font = ImageFont.truetype(
    './font/Inter-3.19/Inter Variable/Inter.ttf', 18)
details_font = ImageFont.truetype(
    './font/Inter-3.19/Inter Variable/Inter.ttf', 14)
title_font.set_variation_by_name('Bold')
details_font.set_variation_by_name('Semi Bold')


def gen_message_and_send_message(event, date, time, venue, alumni_data):
    certi = Image.open('./template.png')
    draw = ImageDraw.Draw(certi)

    W, H = certi.width, certi.height
    w_title, h_title = draw.textsize(alumni_data["name"], font=title_font)
    w_date, h_date = draw.textsize(date, font=details_font)
    w_time, h_time = draw.textsize(time, font=details_font)
    w_venue, h_venue = draw.textsize(venue, font=details_font)

    event_placement = (43, 200)
    date_placement = (42, 253)
    time_placement = (198, 253)
    venue_placement = (42, 305)
    draw.text(
        event_placement,
        event,
        (43, 43, 43),
        font=title_font,
    )
    draw.text(
        date_placement,
        date,
        (43, 43, 43),
        font=details_font,
    )
    draw.text(
        time_placement,
        time,
        (43, 43, 43),
        font=details_font,
    )
    draw.text(
        venue_placement,
        venue,
        (43, 43, 43),
        font=details_font,
    )
    qr = qrcode.QRCode(box_size=4, border=1)
    qr.add_data(json.dumps(alumni_data))
    qr.make()
    qrc = qr.make_image()
    qr_position = ((W - qrc.size[0]) // 2, 338)
    certi.paste(qrc, qr_position)
    path = f"./tickets/{alumni_data['name']}_{event}.png"
    print("Creating at", path)
    certi.save(path)

    account_sid = 'AC42f446ae9255bf244378a329d76991a3'
    auth_token = '1850c071d3feea2c5d3ad127b46ad342'
    client = Client(account_sid, auth_token)

    domain = "https://8f8c-183-82-155-71.in.ngrok.io"
    media_url = f"{domain}/{alumni_data['name'].replace(' ', '%20')}_{event.replace(' ', '%20')}.png"
    print(media_url)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="""Hi {}!,
Here's your admit card for the {} event on {} at {}. Make sure you carry this attachment on your devices as you will be required to show them at the gate.
Looking forward to seeing you there!

Delhi Public School, R.K. Puram
        """.format(alumni_data["name"], event, date, venue),
        to='whatsapp:+917701822620',
        media_url=[media_url]
    )

    print(message.sid)


"""
alumni_data: {
  id: number
  name: string
  passing_year: number
  gender: string
  mobile: string
  number_of_members: string
  event_id: string
}
"""

gen_message_and_send_message("DPS RKP - Back to School", "Thu, 18 Aug 2022", "16:00-21:00", "Delhi Public School, R.K. Puram", {
    "id": 4,
    "name": "Rahul Chandola",
    "passing_year": 1991,
    "gender": "MALE",
    "mobile": "+917701822620",
    "number_of_members": 4,
    "event_id": 2
})
