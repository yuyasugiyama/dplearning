class PostsController < ApplicationController
  def index
    @posts = Post.all.order(created_at: 'desc')
  end
  
  def show
    @post = Post.find(params[:id])
  end
  
  def new
  end
  
  def create
    #render plain: params[:post].inspect
    #save
    @post = Post.new(post_params)
    @post.save!
    #redirect
    redirect_to action: 'show'
  end

  private
    def post_params
       params.require(:post).permit(:title,:image)
    end
end
