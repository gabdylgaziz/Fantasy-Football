import { Component, OnInit } from '@angular/core';
import { Player } from '../players';
import { GK, MF, DF, FW } from '../players';

@Component({
  selector: 'app-fantasy',
  templateUrl: './fantasy.component.html',
  styleUrls: ['./fantasy.component.css']
})
export class FantasyComponent implements OnInit {
  GK = GK
  MF = MF 
  DF = DF 
  FW = FW
  type: string;
  constructor(){
    this.type = 'None';
  }
  ngOnInit(){
    
  }

  change(t: string){
    this.type = t;
  }

  reset(){
    this.type = 'None';
  }
}
