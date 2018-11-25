function dropOffRealTime() {
    if($('#id_external_dropoff_real_time').val().length > 0) {
        $('#id_external_dropoff_abs_time').prop('disabled', true);
    } else {
        $('#id_external_dropoff_abs_time').prop('disabled', false);
    }
}

function dropOffAbsTime() {
    if($('#id_external_dropoff_abs_time').val().length > 0) {
        $('#id_external_dropoff_real_time').prop('disabled', true);
    } else {
        $('#id_external_dropoff_real_time').prop('disabled', false);
    }
}
function internalDropOffRealTime() {
    if($('#id_internal_dropoff_real_time').val().length > 0) {
        $('#id_internal_dropoff_abs_time').prop('disabled', true);
    } else {
        $('#id_internal_dropoff_abs_time').prop('disabled', false);
    }
}

function internalDropOffAbsTime() {
    if($('#id_internal_dropoff_abs_time').val().length > 0) {
        $('#id_internal_dropoff_real_time').prop('disabled', true);
    } else {
        $('#id_internal_dropoff_real_time').prop('disabled', false);
    }
}
function appendToGPSSchedule() {
    $('.gps_schedule').append("<label class='col-form-label tick-left class_own_gps'>" +
        "<label for='id_own_gps'>Own GPS schedule: </label>" +
        "</label>" +
        "<input type='checkbox' name='own_gps' id='id_own_gps' class='class_own_gps' onclick='show_own_gps()'>");
}

function appendToVHFSchedule() {
    $('.vhf_schedule').append("<label class='col-form-label tick-left class_own_vhf'>" +
        "<label for='id_own_vhf'>Own VHF schedule: </label>" +
        "</label>" +
        "<input type='checkbox' name='own_vhf' id='id_own_vhf' class='class_own_vhf' onclick='show_own_vhf()'>");
}

function show_own_gps() {
    show_and_hide('own_gps_schedule')
}

function show_own_vhf() {
    show_and_hide('own_vhf_schedule')
}

function show_and_hide(class_name) {
    if ($('.' + class_name ).css('display') === 'none') {
        $('.' + class_name).show();
    } else {
        $('.' + class_name).hide();
    }
}

function same_addr_function() {
    show_and_hide('delivery');
}