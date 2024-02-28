// Timer function
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = 0; // Set timer to 0 when it reaches negative values
            // You can add additional logic here when the timer reaches 0
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', function () {
    // Set the duration for each question (in seconds)
    var duration = 60;
    
    // Iterate over each timer and start it
    document.querySelectorAll('.timer').forEach(function (timerElement) {
        startTimer(duration, timerElement);
    });
});
