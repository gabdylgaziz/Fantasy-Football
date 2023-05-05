import { Component, OnInit } from '@angular/core';
import { User } from '../user';

@Component({
  selector: 'app-signup-form',
  templateUrl: './signup-form.component.html',
  styleUrls: ['./signup-form.component.css']
})
export class SignupFormComponent implements OnInit  {
  sign: boolean;
  public user: any;
  constructor() {
    this.sign = false;
  }

  nextstep(){
    this.sign = true;
    console.log(this.user)
  }

  prevstep(){
    this.sign = false;
  }



  ngOnInit() {
    this.user = {
      firstname: '',
      lastname: '',
      email: '',
      password: '',
      gender: '',
      birth: 0,
      country: '',
      team: ''
    }
  }


}
