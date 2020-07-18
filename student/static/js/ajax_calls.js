
function ajax_request(input_id,req_url,span_id)
{
    var value = document.getElementById(input_id).value;
    var param = "value="+value
    var request = new XMLHttpRequest;
    request.onreadystatechange = check;
    request.open("POST",req_url,span_id);
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    request.send(param);

    function check()
    {
        if (request.readyState == 4)
        {
            var json_data = JSON.parse(request.responseText);
            sp = document.getElementById(span_id);

            if (json_data.error != undefined)
            {
                sp.style.color = "red";
                sp.innerText = json_data.error;
                document.getElementById('button').disabled = true;
            }
            else
            {
                sp.style.color = "green";
                sp.innerText = json_data.message;
                document.getElementById('button').disabled = false;
            }
        }
    }
}


$(function () {
  $('[data-toggle="popover"]').popover()
})

$(function () {
    $('.example-popover').popover({
        container: 'body'
    })
})