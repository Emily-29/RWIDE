clear;
dehazeName = '\SLP';
folderName = '\02_beta2';
rootPath = 'D:\Dataset\03_RWIDE';
folderPath = [rootPath folderName '\hazy_align'];
SaveFolderPath = [rootPath folderName '\dehaze' dehazeName];
if ~isfolder(SaveFolderPath)
    mkdir(SaveFolderPath);
end

count = 0;
total_time = 0;
dirInfo = dir(folderPath);
for i = 3:length(dirInfo)
    itemName = dirInfo(i).name;
    imagePath = fullfile(folderPath, itemName);
    savePath = fullfile(SaveFolderPath, itemName);

    tic;
    ret = SLP(imagePath);
    elapsed_time = toc;

    total_time = total_time + elapsed_time;
    count = count + 1;
    imwrite(ret, savePath);
    disp(imagePath);
end
average_time = total_time / (length(dirInfo) - 2);
disp(['Average time: ', num2str(average_time), ' seconds']);
