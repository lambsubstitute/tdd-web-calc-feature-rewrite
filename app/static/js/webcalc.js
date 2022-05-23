$(document).ready(function() {

    // Setup
    var socket = io();
    var sign = "";
    var value = 0;
    
    socket.on('connect', function() {
        console.log('Connected to web app');
        console.log('Initialising');
        socket.emit('command', {command: 'intialise'});
    })
    socket.on('response', function(response) {
        $('div#value').text(response.value);
        $('div#calculation').text(response.calculation);

        // Display error if provided
        if ("error" in response) {
            $('div#error').text(response.error);
            $('div#error').show();
        } else {
            $('div#error').text("");
            $('div#error').hide();
        }
    })

    // Numbers
    $('div#zero').click(function(event) {
        socket.emit('command', {command: 0});
        console.log('Sent command: 0');
        return false;
    });
    $('div#one').click(function(event) {
        socket.emit('command', {command: 1});
        console.log('Sent command: 1');
        return false;
    });
    $('div#two').click(function(event) {
        socket.emit('command', {command: 2});
        console.log('Sent command: 2');
        return false;
    });
    $('div#three').click(function(event) {
        socket.emit('command', {command: 3});
        console.log('Sent command: 3');
        return false;
    });
    $('div#four').click(function(event) {
        socket.emit('command', {command: 4});
        console.log('Sent command: 4');
        return false;
    });
    $('div#five').click(function(event) {
        socket.emit('command', {command: 5});
        console.log('Sent command: 5');
        return false;
    });
    $('div#six').click(function(event) {
        socket.emit('command', {command: 6});
        console.log('Sent command: 6');
        return false;
    });
    $('div#seven').click(function(event) {
        socket.emit('command', {command: 7});
        console.log('Sent command: 7');
        return false;
    });
    $('div#eight').click(function(event) {
        socket.emit('command', {command: 8});
        console.log('Sent command: 8');
        return false;
    });
    $('div#nine').click(function(event) {
        socket.emit('command', {command: 9});
        console.log('Sent command: 9');
        return false;
    });
    $('div#decimalplace').click(function(event) {
        socket.emit('command', {command: "."});
        console.log('Sent command: .');
        return false;
    });

    // Modifiers
    $('div#sign').click(function(event) {
        socket.emit('command', {command: "sign"});
        console.log('Sent command: sign');
        return false;
    });

    // Operators
    $('div#clear').click(function(event) {
        socket.emit('command', {command: "clear"});
        console.log('Sent command: clear');
        return false;
    });
    $('div#percent').click(function(event) {
        socket.emit('command', {command: "%"});
        console.log('Sent command: %');
        return false;
    });
    $('div#divide').click(function(event) {
        socket.emit('command', {command: "/"});
        console.log('Sent command: /');
        return false;
    });
    $('div#multiply').click(function(event) {
        socket.emit('command', {command: "*"});
        console.log('Sent command: *');
        return false;
    });
    $('div#subtract').click(function(event) {
        socket.emit('command', {command: "-"});
        console.log('Sent command: -');
        return false;
    });
    $('div#add').click(function(event) {
        socket.emit('command', {command: "+"});
        console.log('Sent command: +');
        return false;

    });
    $('div#equals').click(function(event) {
        socket.emit('command', {command: "="});
        console.log('Sent command: =');
        return false;
    });
})