$(function() {
    function getBarColor( percent )
    {
        if ( percent <= 20 )
            return '#D04343';
        if ( percent <= 30 )
            return '#FF5252';
        else if( percent <= 40)
            return '#FF6B46';
        else if( percent <= 50)
            return '#FFAF58';
        else if( percent <= 60)
            return '#FFD041';
        else if( percent <= 80)
            return '#98FF54';
        else if( percent <= 90)
            return '#47E544';
        else if( percent <= 100)
            return '#3FE5C1';
    }
    $('.chart').each(function()
                {
                    $(this).easyPieChart({
                        size:140,
                        animate: 2000,
                        lineCap:'butt',
                        scaleColor: false,
                        barColor: getBarColor($(this).attr('data-percent')),
                        trackColor: 'transparent',
                        lineWidth: 1
                    });
                });
});
