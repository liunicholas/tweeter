import React from "react";
import { View, Text, Button, TouchableOpacity, StyleSheet } from "react-native";

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
    <View style={styles.card}>
      {/* Display the post content */}
      <Text style={styles.content}>{content}</Text>
      <Text style={styles.likesCount}>Likes: {likes}</Text>
      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={[styles.button, styles.likeButton]}
          onPress={onLike}
        >
          <Text style={styles.buttonText}>Like</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.deleteButton]}
          onPress={onDelete}
        >
          <Text style={[styles.buttonText, styles.deleteButtonText]}>
            Delete
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

// Styles for the PostCard component
const styles = StyleSheet.create({
  // Main card container
  card: {
    backgroundColor: "#ffffff",
    borderRadius: 8,
    padding: 16,
    marginVertical: 8,
    // iOS shadow
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    // Android shadow
    elevation: 3,
  },
  // Post content text
  content: {
    fontSize: 16,
    marginBottom: 12,
    lineHeight: 24,
  },
  // Likes counter text
  likesCount: {
    fontSize: 14,
    color: "#666",
    marginBottom: 12,
  },
  // Like button specific styles
  likeButton: {
    backgroundColor: "#4CAF50",
  },
  // Container for action buttons
  buttonContainer: {
    flexDirection: "row",
    justifyContent: "space-between",
  },
  // Base button styles
  button: {
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderRadius: 4,
    flex: 1,
    marginHorizontal: 4,
    alignItems: "center",
  },
  // Button text base style
  buttonText: {
    color: "#fff",
    fontWeight: "600",
  },
  // Delete button specific styles
  deleteButton: {
    backgroundColor: "#fff",
    borderWidth: 1,
    borderColor: "#ff5252",
  },
  // Delete button text specific style
  deleteButtonText: {
    color: "#ff5252",
  },
});
