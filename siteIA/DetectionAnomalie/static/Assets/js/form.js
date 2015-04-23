$(document).ready(function()
{
    $("#select").multiselect({
        maxHeight: 200
    });

    var cache = $("#cache");

    cache.val("");
    $('ul').children(1).each(function(index)
    {
       if($(this).attr('class')=="active")
       {
        if(index > 0)
        {
            cache.val(cache.val()+','+index-2);
        }
       }
    });

    $("#select").change(function()
    {
        cache.val("");
        $('ul').children(1).each(function(index)
        {
           if($(this).attr('class')=="active")
           {
            if(index > 0)
            {
                cache.val(cache.val()+','+index-2);
            }
           }
        });
    });
    var i=1;
    $('input:checkbox').each(function()
    {
        if(i>=5)
        {
            $(this).prop("checked",true);
        }
        i++;
    });

    $("#clear").click(function()
    {
         $('input:checkbox').each(function()
        {
            $(this).removeAttr('checked');
        });
    });

    $("#reset").click(function()
    {
        var i=1;

        $('input:checkbox').each(function()
        {
            if(i>=5)
            {
                $(this).prop("checked",true);
            }
            i++;
        });
    });
});
