$(document).ready(function()
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
