
    $(document).on('submit','#add_cart',function(e){
        e.preventDefault();
        $.ajax({

            url:"/add-to-cart/",
            type:"POST",


            data:{
                product_id:$('#product_id').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function () {
                alert("Added to Cart");
            },
           error: function(e){
                alert(e);

            }

        });

    });

