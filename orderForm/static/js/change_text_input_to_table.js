function changeToTable() {
    if(!$('table').hasClass('sim_info')) {

        var quantity = getQuantity();
        var table_data = '';
        var telephone_nums = $('#telno').text().trim().split('$');
        var pins = $('#pin').text().trim().split('$');
        var puks = $('#puk').text().trim().split('$');

        for(var i=0; i < quantity; i ++) {
            var stringI = i.toString();
            table_data += '<tr>' +
                '<td><input type="text" class="telephone_no" value="' + telephone_nums[i] + '"></td>' +
                '<td><input type="text" class="sim_pin" value="' + pins[i] + '"></td>' +
                '<td><input type="text" class="sim_puk" value="' + puks[i] + '"></td>' +
                '</tr>'
        }

        var table = '<table class="sim_info">' +
            '<thead>' +
            '<tr>' +
            '<th>sim telephone no</th>' +
            '<th>sim pin</th>' +
            '<th>sim puk</th>' +
            '</tr>' +
            '</thead>' +
            table_data +
            '</table>';

        $('.extra_gsm').hide();

        $('.own_sim').append(table);
        $('.own_sim').show();
        $('#id_gsm_customer_sim_telephone_no').prev().hide();
        $('#id_gsm_customer_sim_telephone_no').hide();
    } else {
        $('.sim_info').remove();
        changeToTable();
    }
}

function convertToInt(x) {
    var val = parseInt(x);
    return isNaN(val) ? 0: val;
}

function getQuantity() {
    var val1 = convertToInt($('#id_form-0-number_of_collars').val());
    var val2 = convertToInt($('#id_form-1-number_of_collars').val());
    var val3 = convertToInt($('#id_form-2-number_of_collars').val());
    var val4 = convertToInt($('#id_form-3-number_of_collars').val());

    var quantity = (val1 + val2 + val3 + val4);

    return quantity;
}

function writeTableDataIntoFormelement() {
    var numbers = [];
    var pins = [];
    var puks = [];
    var quantity = getQuantity();

    $('.sim_info .telephone_no').each(function () {
        if($(this).val() !== '') {
            numbers.push($(this).val());
        }
    });

    $('.sim_info .sim_pin').each(function () {
        if($(this).val() !== '') {
            pins.push($(this).val());
        }
    });

    $('.sim_info .sim_puk').each(function () {
        if($(this).val() !== '') {
            puks.push($(this).val());
        }
    });

    if(numbers.length !== quantity && $('#id_gsm_customer_sim_telephone_no').val() === '' && $('table').hasClass('sim_info')) {
        alert('Please fill out all sim table rows');
    } else {
        $('#id_gsm_customer_sim_telephone_no').val(numbers.join('$'));
        $('#id_gsm_customer_sim_pin').val(pins.join('$'));
        $('#id_gsm_customer_sim_puk').val(puks.join('$'));
    }
}