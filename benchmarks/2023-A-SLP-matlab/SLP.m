function ret = SLP(path)
I = imread(path);
ret = dehaze_slp(I);