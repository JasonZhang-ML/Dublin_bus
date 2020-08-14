## Dublin Bus
Dublin bus is a web based app which can predict time spend from the original stop to the destination stop.


###Running instruction

This core of application is based on Flask. Please find the Flask folder in the src folder and enter `flask run` in the terminal to start the service.


Since our trained models exceed 12GB, it's impossible to submit them together. You may check our models on the server provided by the UCD or go to the website to check the application.


### Front end code
The front-end code is based on Vue and Vue-CLI. The code that I programmed in the "FrontEnd" file are uncompiled. After finishing, I use Webpack to bundle my code. The bundled code is static assets and they are in the Flask template and static folder.

If you want to run the front-end code separately, please open the folder at  `src/FrontEnd/uncomplied_FE_code`, and run `npm install` in the terminal to install the required dependencies. Then run `npm run serve` to initiate the application.


### Author    
- Wenqin Yang (Back-end)
- Jiansheng Zhang (Modeling)
- Bowen Wang (Front-end)
- Cheng Qain (Maintaining)
