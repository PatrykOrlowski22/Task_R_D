# Task_R_D
Task from R&D

This code solves the problem of finding and selecting an object in a movie.
This code executes it in two classes that are threads. Thread A reads the source video file and sends it to thread B frame by frame in a queue. 
In class B receives the frames and finds the position of the sample.png file on them by marking it with a rectangle. 
Through the queue, thread B sends the coordinates to main() where the frames are saved as a *_X_Y.png file in a new "processed" folder.

## Contribute

* Source Code: github.com/PatrykOrlowski22/Task_R_D

## License

The Unlicense

## Author 

Patryk Orłowski
