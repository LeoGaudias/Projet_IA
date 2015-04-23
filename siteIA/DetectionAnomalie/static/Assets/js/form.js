$(document).ready(function()
{
    $("#select").multiselect({
        maxHeight: 200,
    });

    var cache = $("#cache");

    function maj_cache()
    {
        cache.val('{"data":[');
        $('ul').children(1).each(function(index)
        {
           if($(this).attr('class')=="active")
           {
            if(index > 0)
            {
                if(cache.val()=='{"data":[')
                {
                    cache.val(cache.val()+'{"id":'+(parseInt(index)-2)+',"value":"'+$(this).text()+'"}');
                }
                else
                {
                    cache.val(cache.val()+',{"id":'+(parseInt(index)-2)+',"value":"'+$(this).text()+'"}');
                }
            }
           }
        });
        cache.val(cache.val()+"]}");
        cache.val(JSON.stringify(cache.val()));
    }

    maj_cache();

    $("#select").change(function()
    {
        maj_cache();
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
         /*$('input:checkbox').each(function()
        {
            $(this).removeAttr('checked');
        });*/

        $('#select').multiselect('deselectAll', false);
        $('#select').multiselect('updateButtonText');
        cache.val("");
    });

    $("#reset").click(function()
    {
        /*var i=1;

        $('input:checkbox').each(function()
        {
            if(i>=5)
            {
                $(this).prop("checked",true);
            }
            i++;
        });*/

        $('#select').multiselect('select', ['src_bytes', 'dst_bytes', 'land']);
        maj_cache();
    });
});
