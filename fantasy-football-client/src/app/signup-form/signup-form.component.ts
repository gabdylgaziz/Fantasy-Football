import { Component } from '@angular/core';
import { User } from '../user';

@Component({
  selector: 'app-signup-form',
  templateUrl: './signup-form.component.html',
  styleUrls: ['./signup-form.component.css']
})
export class SignupFormComponent {
  sign: boolean;
  user: User[];
  constructor() {
    this.sign = false;
    this.user = [];
  }

  nextstep(){
    this.sign = true;
  }

  prevstep(){
    this.sign = false;
  }

  onSubmit(name: string,surname: string,email: string,password: string,date: string,){
    console.log(name)
    console.log(surname)
    console.log(email)
    console.log(password)
    console.log(date)
  }



}
