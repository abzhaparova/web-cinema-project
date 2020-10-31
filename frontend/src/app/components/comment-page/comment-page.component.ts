import {AfterViewInit, Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {MovieService} from '../../services/movie.service';
import { CommentPage } from '../../commentPage';
import { CommentService } from '../../services/comment.service';
import { Comment } from '../../comment';
import {HttpClient} from '@angular/common/http';
import {TokenStorageService} from '../../services/token-storage.service';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-comment-page',
  templateUrl: './comment-page.component.html',
  styleUrls: ['./comment-page.component.css']
})
export class CommentPageComponent implements OnInit {
  constructor(public commentService: CommentService,
              public tokenStorageService: TokenStorageService) { }

  @Input() PAGE_ID: number;
  comments: Comment[];
  showCommentForm = false;
  message: string;

  ngOnInit(): void {
    this.commentService.getComments(this.PAGE_ID).subscribe(res => this.comments = res);
    console.log(this.tokenStorageService.getToken());
  }

  showForm(): void {
    if (this.tokenStorageService.getToken() === null) {
      alert('You need to login to write comments');
    } else {
      this.showCommentForm = true;
    }
  }

  changeVote(commentId: number, delta: number) {
    this.commentService.updateComment(commentId, delta);
  }

  writeComment(): void {
    this.commentService.writeComment(this.message, this.PAGE_ID);
    window.location.reload();
  }

  deleteComment(id: number): void {
    this.commentService.deleteComment(id);
  }
}
