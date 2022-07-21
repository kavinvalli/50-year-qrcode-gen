const accountSid = "AC42f446ae9255bf244378a329d76991a3";
const authToken = "[Redacted]";
const client = require("twilio")(accountSid, authToken);

client.messages
  .create({
    body: "Your Twilio code is 1238432",
    from: "whatsapp:+14155238886",
    to: "whatsapp:+917701822620",
  })
  .then((message) => console.log(message.sid))
  .done();
