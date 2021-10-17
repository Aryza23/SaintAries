const fetch = require("node-fetch")

let kuki_name;

let kuki_owner;

class Kukibot {

  constructor(options = {name: 'kuki', owner:'moezilla'}){

        kuki_name = options.name;

        kuki_owner = options.owner;

    }

  async moe(message) {

    if(!message) {

      throw new Error("[Kuki-Bot-API: ERROR] Query paramter must be a string")

    }

    let json = await fetch(`https://www.kukiapi.xyz/api/apikey=KUKItg111XlOZ/message=${encodeURIComponent(message)}`)

    let kuki = await json.json()

    if(!kuki) {

      throw new Error("[Kuki-Bot-API: ERROR] Query parameter must be passed")

    }

    return kuki.reply.replace('kuki', kuki_name).replace('MoeZilla', kuki_owner);

  }

}

module.exports = Kukibot
