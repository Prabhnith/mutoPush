// Load modules
var restify = require('restify');


function respond(req,res,next){
console.log("In respond")
var apn = require('apn');

// Replace these with your own values.
var cert = "E:/Developer/mutoPush/cert.pem";
var key = "E:/Developer/mutoPush/key.pem";
var deviceID = req.params.deviceID;

var service = new apn.Connection({
    cert: cert,
    key: key
});


var myDevice = new apn.Device(deviceID);
var note = new apn.Notification();


note.expiry = Math.floor(Date.now() / 1000) + 3600; // Expires 1 hour from now.
note.alert = "This is a notification that will be displayed ASAP.";


service.pushNotification(note, myDevice);


res.send('Message sent to '+ req.params.deviceID)
next();
}




var server = restify.createServer();
server.get('/apns/:deviceID', respond);
server.head('/apns/:deviceID', respond);


server.listen(8080,function(){
console.log('%s listening at %s', server.name, server.url);
});
