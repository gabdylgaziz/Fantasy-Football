import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { LoginComponent } from './login/login.component';
import { ToptableComponent } from './toptable/toptable.component';
import { NewsComponent } from './news/news.component';
import { FooterComponent } from './footer/footer.component';
import { SignupFormComponent } from './signup-form/signup-form.component';
import { FantasyComponent } from './fantasy/fantasy.component';

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    LoginComponent,
    ToptableComponent,
    NewsComponent,
    FooterComponent,
    SignupFormComponent,
    FantasyComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
