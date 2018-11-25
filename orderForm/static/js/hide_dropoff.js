$(document).ready(function() {
    if ($('#id_external_dropoff').is(':checked')) {
        $('.dropoff').show();
    } else {
        $('.dropoff').hide();
    }

    if ($('#id_internal_dropoff').is(':checked')) {
        $('.internal_dropoff').show();
    } else {
        $('.internal_dropoff').hide();
    }

    if ($('#id_iridium').is(':checked')) {
        show_and_hide('iridium');
    }

    if ($('#id_belt_labeling').is(':checked')) {
        $('.label_instructions').show();
    } else {
        $('.label_instructions').hide();
    }

    if($('#id_belt_plates').is(':checked')) {
        $('.plate_instructions').show();
    } else {
        $('.plate_instructions').hide();
    }

    if(!$('#id_external_dropoff').is(':checked')) {
        $('.dropoff').hide();
    }

    if($('#timezone option:selected').text() != 'LMT') {
        $('.utc-correction').hide();
    }

    if($('#id_iridium').is(':checked')) {
        $('#id_globalstar').parent().hide();
        $('#id_groundstation_number').parent().hide();
        $('.gsm').hide();
        $('.sob').hide();
        $('.sim_info').hide();
    }

    if($('#id_globalstar').is(':checked')) {
        $('.iridium').hide();
        $('#id_iridium').parent().hide();
        $('#id_groundstation_number').parent().hide();
        $('.gsm').hide();
        $('.sob').hide();
        $('.sim_info').hide();
    }

    if($('#id_gsm').is(':checked')) {
        $('#id_globalstar').parent().hide();
        $('.iridium').hide();
        $('#id_iridium').parent().hide();
        $('.sob').hide();

        if($('#id_gsm_vectronic_sim').is(':checked')) {
            $('#id_groundstation_number').parent().hide();
            $('#id_gsm_customer_sim_telephone_no').parent().hide();
            $('#id_gsm_customer_sim_pin').parent().hide();
            $('#id_gsm_customer_sim_puk').parent().hide();
        } else {
            $('#id_groundstation_number').parent().show();
            changeToTable();
        }
    }

    if($('#id_store_on_board').is(':checked')) {
        $('#id_globalstar').parent().hide();
        $('.iridium').hide();
        $('#id_iridium').parent().hide();
        $('.gsm').hide();
    }

    $('.last_step').mouseover(function () {
        writeTableDataIntoFormelement();
    })
});

function dropoff_function() {
    if($('.dropoff').css('display') == 'none') {
        $('.dropoff').show();
    } else {
        $('.dropoff').hide();
    }
}

function internal_dropoff_function() {
    if($('.internal_dropoff').css('display') == 'none') {
        $('.internal_dropoff').show();
    } else {
        $('.internal_dropoff').hide();
    }
}

function lable_function() {
    if($('.label_instructions').css('display') == 'none') {
        $('.label_instructions').show();
    } else {
        $('.label_instructions').hide();
    }
}

function plates_function() {
    if($('.plate_instructions').css('display') == 'none') {
        $('.plate_instructions').show();
    } else {
        $('.plate_instructions').hide();
    }
}

function timezone_function() {
    if($('#timezone option:selected').text() == 'LMT') {
        $('.utc-correction').show();
    } else {
        $('.utc-correction').hide();
    }
}

function iridium_function() {
   if($('.iridium').css('display') === 'none') {
        $('.iridium').show();
        $('#id_globalstar').prop('checked', false);
        $('#id_gsm').prop('checked', false);
    } else {
        $('.iridium').hide();
        $('#id_globalstar').show();
        $('#id_gsm').show();
    }
}

function gsm_function() {
   if(!$('table').hasClass('sim_info')) {
       //$('.extra_gsm').show();
       if(!$('#id_gsm_vectronic_sim').is(':checked')) {
           $('#id_groundstation_number').parent().show();
           changeToTable();
       }
    } else {
       $('#id_groundstation_number').parent().hide();
       $('.sim_info').remove();
       // $('.extra_gsm').hide();
       // $('#id_gsm_customer_sim_telephone_no').val('');
       // $('#id_gsm_customer_sim_pin').val('');
       // $('#id_gsm_customer_sim_puk').val('');
    }
}

function checkAmount(){
    if ($('#id_form-0-battery_size').val() == '') {

    }
}

