import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from './components/home/home.component';
import {MovieDetailsComponent} from './components/movie-details/movie-details.component';
import {UserProfileComponent} from './components/user-profile/user-profile.component';
import {SearchComponent} from './components/search/search.component';
import {AuthGuard} from './auth.guard';


const routes: Routes = [
  { path: 'search', component: SearchComponent },
  { path: 'profile/:name', component: UserProfileComponent },
  { path: 'movies/:id', component: MovieDetailsComponent},
  { path: 'home', component: HomeComponent},
  { path: '', redirectTo: 'home', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
