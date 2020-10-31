import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Movie } from '../../movie';
import { MovieService } from '../../services/movie.service';
import {CommentPageComponent} from '../comment-page/comment-page.component';

@Component({
  selector: 'app-movie-details',
  templateUrl: './movie-details.component.html',
  styleUrls: ['./movie-details.component.css']
})
export class MovieDetailsComponent implements OnInit {
  movie: Movie = null;
  PAGE_ID: number = null;
  constructor(private route: ActivatedRoute, private movieService: MovieService) { }
  ngOnInit(): void {
    this.getMovie();
  }
  getMovie(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.movieService.getMovieById(id).subscribe(
      movie => {
        this.movie = movie;
        this.PAGE_ID = this.movie.comment_page_id;
      }
    );

  }

}
