import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
<<<<<<< HEAD
import { NavBarComponent } from './nav-bar/nav-bar.component';
=======
import { LoginComponent } from './login/login.component';
import { ToptableComponent } from './toptable/toptable.component';
import { NewsComponent } from './news/news.component';
import { FooterComponent } from './footer/footer.component';
>>>>>>> 24b1356edd9bd1d6ebde7ae9b194ae89f8bed16f

@NgModule({
  declarations: [
    AppComponent,
<<<<<<< HEAD
    NavBarComponent
=======
    LoginComponent,
    ToptableComponent,
    NewsComponent,
    FooterComponent
>>>>>>> 24b1356edd9bd1d6ebde7ae9b194ae89f8bed16f
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
