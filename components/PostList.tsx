import React from 'react';
import { View, Text } from 'react-native';
import { PostCard } from './PostCard';

// Define the Post type
interface Post {
  id: string;
  content: string;
  likes: number;
  timestamp: Date;
}

// Define props interface
interface PostListProps {
  posts: Post[];
  onLikePost: (postId: string) => void;
  onDeletePost: (postId: string) => void;
}

// PostList renders the list of posts using the PostCard component
export const PostList: React.FC<PostListProps> = ({
  posts,
  onLikePost,
  onDeletePost,
}) => {
  // If there are no posts, show a message
  if (posts.length === 0) {
    return (
      <View>
        <Text>No posts yet. Be the first to post!</Text>
      </View>
    );
  }

  // Render the list of posts
  return (
    <View>
      {posts.map((post) => (
        <PostCard
          key={post.id}
          content={post.content}
          likes={post.likes}
          onLike={() => onLikePost(post.id)}
          onDelete={() => onDeletePost(post.id)}
        />
      ))}
    </View>
  );
};