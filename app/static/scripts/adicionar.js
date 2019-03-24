function plus(thing){
            var quantity=0;
            // Get the field name
            var quantity = parseInt($('[name="'+thing+'"]').val());
            
            // If is not undefined
            $('[name="'+thing+'"]').val(quantity + 1);
            // Increment
            
        };
    
function minus(thing){
            var quantity=0;
            // Get the field name
            var quantity = parseInt($('[name="'+thing+'"]').val());
            
            // If is not undefined
          
                // Increment
                if(quantity>0){
                    $('[name="'+thing+'"]').val(quantity - 1);
                }
        };
        