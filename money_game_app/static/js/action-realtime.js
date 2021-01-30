$(document).ready(function(){
    $('.gold-form').submit(function(){
        var data = $(this).serialize() 
        $.ajax({
            method: "POST",   
            url: '/process_money',
            data: data
        })
        .done(function(res){
            $("#actions-table").append(res)
        })
        return false
    })
}) 