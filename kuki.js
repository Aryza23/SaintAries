const Slimbot = require('slimbot');
const slimbot = new Slimbot(process.env.token);
const Kukibot = require("./Kuki.js");
const kukiai  =  new  Kukibot({name: (process.env.name), owner: (process.env.owner)});



slimbot.on('message', message => {
var text = message.text
  kukiai.moe(text)
 .then(reply => {
  slimbot.sendMessage(message.chat.id, reply);
 })
if (message.text.toLowerCase()=='/start'){
        slimbot.sendMessage(message.chat.id, "I am kuki");
    }
});


slimbot.startPolling();
