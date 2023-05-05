import { Component, OnInit } from '@angular/core';
import {throwError} from 'rxjs';

@Component({
  selector: 'app-signin-form',
  templateUrl: './signin-form.component.html',
  styleUrls: ['./signin-form.component.css']
})
export class SigninFormComponent {
  public user: any;

 
  ngOnInit() {
    this.user = {
      username: '',
      password: ''
    };
  }
  
  sign(){
    console.log(this.user)
  }
}
