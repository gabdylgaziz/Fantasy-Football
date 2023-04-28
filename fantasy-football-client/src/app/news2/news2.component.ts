import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { leaderbord } from '../leaderboard';
import { Games } from '../schedule';
import { News } from '../news';

@Component({
  selector: 'app-news2',
  templateUrl: './news2.component.html',
  styleUrls: ['./news2.component.css']
})



export class News2Component {
  leaderbord = leaderbord;
  games = Games;
  news = News;
}
