import { Component, OnInit } from '@angular/core';
import {MovieService} from '../../services/movie.service';
import {Movie} from '../../movie';
import {filter, map } from 'rxjs/operators';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  searchTerm: string;
  genres: string[];
  movies: Movie[];
  showResults = false;
  constructor(private movieService: MovieService) { }

  ngOnInit(): void {
  }

  search(): void {
    console.log('here');
    this.searchTerm = this.searchTerm.toLowerCase();
    this.showResults = true;
    this.movieService.getMovies().pipe(map(movie =>
      movie.filter(movief => movief.title.toLowerCase().includes(this.searchTerm)))).subscribe(movies => this.movies = movies);
  }

}
