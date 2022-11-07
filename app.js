var express = require("express");
var bodyParser = require("body-parser");
var mongoose = require("mongoose");
const https = require("https");



const app = express()
 
app.use(bodyParser.json())
app.use(express.static('public'))
app.use(bodyParser.urlencoded({
    extended:true
}))

mongoose.connect('mongodb+srv://admin-dhruv:thakor00@cluster0.hv4rspl.mongodb.net/dhrcoder?retryWrites=true&w=majority',{
    useNewUrlParser: true,
    useUnifiedTopology: true 
});


var db = mongoose.connection;

db.on('error',()=>console.log("Error in conneting"));
db.once('open',()=>console.log("Connected to Database"))


// /////////////////MY SITE/////////////////////

app.get("/", (req,res) => {
    res.sendFile(__dirname + "/public/mysite.html");
});


//////////////////////Sign up form/////////////////////////////


app.post("/sign_up_form/",(req,res)=>{
    var name = req.body.name;
    var email =req.body.email;
    var phone = req.body.phone;
    var password = req.body.password;

    var data = {
        "name" : name,
        "email" : email,
        "phone" : phone,
        "password": password
    }

    db.collection('signup').insertOne(data,(err,collection)=>{
        if(err){
            throw err;
        }
        console.log("Record Inserted Succesfully")
    });

    // return res.redirect('signup_success.html')
    return res.redirect('submit_form/index.html')

})

////////////////////////////////////Contact Me Form/////////////////////////////////

app.post("/contact_me/",(req,res)=>{
    var name = req.body.name;
    var email =req.body.email;
    var message = req.body.message;

    var data = {
        "name" : name,
        "email" : email,
        "message" : message,
    }

    db.collection('contacts').insertOne(data,(err,collection)=>{
        if(err){
            throw err;
        }
        console.log("Record Inserted Succesfully")
    });

    return res.redirect('submit_form/index.html')
})

///////////////////Weather project/////////////////////////





app.post("/projects/weather_project/", function (req, res) {
const query = req.body.cityName;
const apiKey = "050ebe9a8adf2062e79db7a56d1e6d77"
const unit = "metric"
// lat=22.952541&lon=76.031219
const url = "https://api.openweathermap.org/data/2.5/weather?q=" + query + "&appid=" + apiKey + "&units=" + unit;

https.get(url, function (response) {
    console.log("Your HTTP status code is ",response.statusCode);

    response.on("data", function (data) {
        const weatherData = JSON.parse(data)
        const temp = weatherData.main.temp
        const weatherDescription = weatherData.weather[0].description
        const icon = weatherData.weather[0].icon
        const imageURL = "https://openweathermap.org/img/wn/" + icon + "@2x.png"
        res.write("<p>The weather is currently " + weatherDescription + "</p>");
        res.write("<h1>The temperature " + query + " is " + temp + " degrees Celcius </h1>");
        res.write("<img src=" + imageURL + ">")
        res.send()

    })
})

})



///////////////////hosting///////////////////////////////
app.listen(process.env.PORT || 3000 ,() => {
    console.log(__dirname)
    console.log("Server is started successfully")
}); 
