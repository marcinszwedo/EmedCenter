[![LinkedIn][linkedin-shield]][linkedin-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="emed/images/emed.png" alt="Logo" width="260" height="80">
  </a>

  <h3 align="center">Emed Center</h3>
  <p align="center">
    App for ordering regular medications.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

The app was written to make it easier to order regular medications for patients. **No waiting to see the doctor.**

How it's working:
- Each patient is assigned to his own doctor
- The patient orders medicine
- The doctor receives the order, verifies and accepts it 


### Built With

* [![Django][Django.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/marcinszwedo/EmedCenter.git
   $ cd emed
   ```
2. Create a virtual environment to install dependencies in and activate it:
   ```sh
   $ virtualenv2 --no-site-packages env
   $ source env/bin/activate
   ```
3. Install the dependencies
   ```sh
   (env)$ pip install -r requirements.txt
   ```
   Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.
4. Make migrations and run the server
   ```sh
   (env)$ python manage.py migrate
   (env)$ python manage.py runserver
   ```
5. Go to the web browser and enter <a href="[Django-server]">http://127.0.0.1:8000/</a> to verify whether the application is running fine or not.
 





<!-- USAGE EXAMPLES -->
## Usage

There are four access levels:
  1. Patient
  - signing up (the account must be verified by the nurse/receptionist)
  - ordering medicines (account must be verified)
  - viewing order history
  - changing user data (not all)
  2. Nurse/receptionist:
  - verifying user accounts and assigning doctors to them
  - adding medicine to the database
  - assigning doctors
  3. Doctor:
  - view orders only from his patients
  - accepting orders for medicines
  4. Admin:
  - all access

Screenshots
1. Signup
   <a href="[Django-server]">http://127.0.0.1:8000/accounts/user_create/>http://127.0.0.1:8000/accounts/user_create/</a>

2. Signup
   <a href="[Django-server]">http://127.0.0.1:8000/accounts/user_create/>http://127.0.0.1:8000/accounts/user_create/</a>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Your Name - [Marcin Szwedo](www.linkedin.com/in/marcin-szwedo)

Project Link: [https://github.com/marcinszwedo/EmedCenter](https://github.com/marcinszwedo/EmedCenter)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/marcinszwedo/EmedCenter.git?style=for-the-badge
[forks-url]: https://github.com/marcinszwedo/EmedCenter/forks
[stars-shield]: https://img.shields.io/github/stars/marcinszwedo/EmedCenter.git?style=for-the-badge
[stars-url]: https://github.com/marcinszwedo/EmedCenter/stargazers
[license-shield]: https://img.shields.io/github/license/marcinszwedo/EmedCenter.git?style=for-the-badge
<!-- edit -->
[license-url]: https://github.com/marcinszwedo/EmedCenter/LICENSE.txt 
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marcin-szwedo
[product-screenshot]: emed/images/screenshot.PNG
[signup-screenshot]: emed/images/screenshot.PNG
[order-screenshot]: emed/images/screenshot.PNG
[product-screenshot]: emed/images/screenshot.PNG
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Django.com]: https://img.shields.io/badge/DJANGO-%23092E20?style=for-the-badge&logo=django
[Django-url]: https://www.djangoproject.com/
[Django-server]: http://127.0.0.1:8000/

