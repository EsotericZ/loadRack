
//$(document).ready(function(){
//    //connect to the socket server.
//    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
//    var numbers_received = [];

//    //receive details from server
//    socket.on('newnumber', function(msg) {
//        console.log("Received number" + msg.number);
//        maintain a list of ten numbers
//         if (numbers_received.length >= 8){
//             numbers_received.shift()
//         }
//         numbers_received.push(msg.number);
//         numbers_string = '';
//         for (var i = 0; i < numbers_received.length; i++){
//             numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
//         }
//         $('#log').html(numbers_string);
//    });

//});

$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        // console.log("Received number" + msg.number);
        var data = msg.number.toString();
        data = data.split(',');
        console.log(data);
        // $('#log').html(msg.number.toString());
        $('#log1').html(data[0]);
        $('#log2').html(data[1]);
        $('#log3').html(data[2]);
        $('#log4').html(data[3]);
        $('#log5').html(data[4]);
    });

});
