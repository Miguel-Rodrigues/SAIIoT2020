$(document).ready(function () {
    var joypad = nipplejs.create({
        zone: $("#joypad")[0],
        mode: 'static',
        position: {left: '50%', top: '50%'},
        color: 'red',
        
    });

    joypad.on("move", function(evt, data) {
        controls.pitch = data.force*Math.cos(data.angle.radian);
        controls.roll = data.force*Math.sin(data.angle.radian);
        MoveKart();
    });

    $("#button1").mousedown(function () {
        controls.button1 = true;
        MoveKart();

    });

    $("#button1").mouseup(function () {
        controls.button1 = false;
        MoveKart();
    });

    $("#button2").mousedown(function () {
        controls.button2 = true;
        MoveKart();
    });

    $("#button2").mouseup(function () {
        controls.button2 = false;
        MoveKart();
    });
    
    var refresh = true;
    var controls = {
        nam : "Web controller"
        gyro : { x: 0, y: 0, z: 0 }
        accel : { x: 0, y: 0, z: 0 }
        compass : { x: 0, y: 0, z: 0 }
        pitch : 0,
        roll : 0,
        heading : 0,
        button1: false,
        button2: false
    };

    function MoveKart() {
        if (refresh) {
            refresh = false;
            setTimeout(function() {
                refresh = true;
            }, 200);
    
            $.post("/AccelKartServer/api/moveKart/", controls)
                .done(function(data, textStatus) {
                    $("#output").val(
                        $("#output").val() +
                        "[" + new Date().toISOString() + "][" + textStatus + "] Got response: " + JSON.stringify(data) + "\n");
                })
                .fail(function(xhr, textStatus) {
    
                    $("#output").val(
                        $("#output").val() + "\n" +
                        "[" + new Date().toISOString() + "][" + textStatus + "] Failed to get response: " + xhr.responseText + "\n");
                });
        }
    }
});