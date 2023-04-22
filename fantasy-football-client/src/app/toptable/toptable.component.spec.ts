import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToptableComponent } from './toptable.component';

describe('ToptableComponent', () => {
  let component: ToptableComponent;
  let fixture: ComponentFixture<ToptableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ToptableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ToptableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
