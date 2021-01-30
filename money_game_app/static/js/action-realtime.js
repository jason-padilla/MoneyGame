$(document).ready(function(){
    $('.gold-form').submit(function(){
        var data = $(this).serialize() 
        $.ajax({
            method: "POST",   
            url: '/process_money',
            data: data
        })
        .done(function(res){
            console.log("yes")
            console.log(res)
            $("#actions-table").append(res)
        })
        return false
    })
}) 