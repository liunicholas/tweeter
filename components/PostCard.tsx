import React from 'react';
import { View, Text, Button } from 'react-native';

// Define the props interface to ensure type safety
interface PostCardProps {
  content: string;
  likes: number;
  onLike: () => void;
  onDelete: () => void;
}

// PostCard is a presentational component that displays a single post
// It receives data and callbacks as props from its parent component
export const PostCard: React.FC<PostCardProps> = ({
  content,
  likes,
  onLike,
  onDelete,
}) => {
  return (
    <View>
      {/* Display the post content */}
      <Text>{content}</Text>
      
      {/* Display the number of likes */}
      <Text>Likes: {likes}</Text>
      
      {/* Action buttons */}
      <Button title="Like" onPress={onLike} />
      <Button title="Delete" onPress={onDelete} />
    </View>
  );
};