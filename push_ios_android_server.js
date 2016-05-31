// Load modules
var restify = require('restify');

// FOR MUTO PUSH 
//API_KEY_ANDROID = "AIzaSyBfI5t4-GW5VovfzQ6BpvhTd2dkUB7L9R0";

//FOR pushNotifications
API_KEY_ANDROID = "AIzaSyAs_Z5wBfZO0wZufXkzXOvunRA04tjRIUM"

function receivetoken(req,res,next){
	console.log("In receivetoken");
	var devicePlatform = req.body.devicePlatform;
	var deviceId = req.body.deviceId;
	console.log(devicePlatform,deviceId)

	if (devicePlatform == 'iOS'){
		console.log("In iOS")
		//APNS code goes here
		var apn = require('apn');

		// Replace these with your own values.
		var cert = "E:/Developer/mutoPush/cert.pem";
		var key = "E:/Developer/mutoPush/key.pem";
		

		var service = new apn.Connection({
		    cert: cert,
		    key: key
		});

		var myDevice = new apn.Device(deviceId);
		var note = new apn.Notification();

		note.expiry = Math.floor(Date.now() / 1000) + 3600; // Expires 1 hour from now.
		note.alert = "This is a notification that will be displayed ASAP.";

		service.pushNotification(note, myDevice);
		console.log("Message Sent to iOS device: "+ deviceId); // TODO: Post it to a URL to maintain a log of all the requests sent.

	}

	if (devicePlatform == 'Android'){
		console.log("In Android");
		// GCM Code goes here
		var gcm = require('node-gcm');

		// Replace these with your own values.
		var apiKey = API_KEY_ANDROID;

		var service = new gcm.Sender(apiKey);
		var message = new gcm.Message();
		message.addData('title', 'Hello, World');
		message.addData('body', 'This is a notification that will be displayed ASAP.');

		service.send(message, { registrationTokens: [ deviceId ] }, function (err, response) {
			if(err) console.error(err);
			else 	console.log(response);
		});

		console.log("Message Sent to Android device: "+ deviceId);


		}

	
	return next();
}

var server = restify.createServer();
server.use(restify.bodyParser());  // REQUIRED FOR PARSING JSON
server.post('/receivetoken',receivetoken);


server.listen(8080,function(){
	console.log('%s listening at %s', server.name, server.url);
});
